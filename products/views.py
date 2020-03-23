from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductCreateForm, RawProductForm
# Create your views here.


# def product_create_view(request):
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     else:
#         my_form = RawProductForm()
#     context = {
#         'form': my_form
#     }
#     return render(request, 'products/create.html', context)

# def render_initial_data(request):
#     initial_data = {
#         'title': 'Initial Title',
#         'price': 2.5,
#         'mrp': 3,
#         'featured': True
#     }
#     form = RawProductForm(request.POST or None, initial=initial_data)
#     context = {
#         'form': form
#     }
#     return render(request, '', context)


# def render_database_data(request):
#     product = Product.objects.get(id=3)
#     form = RawProductForm(request.POST or None, instance=product)
#     if form.is_valid():
#         form.save()  # We are able to use this method because form is instance of database object
#     context = {
#         'form': form
#     }
#     return render(request, '', context)

# def handling_object_404(request, my_id):
#     # 1st way
#     obj = get_object_or_404(Product, id=id)
#     # 2nd way
#     try:
#         obj = Product.objects.get(id=my_id)
#     except Product.DoesNotExist:
#         raise Http404
#     context = {
#         'object': obj
#     }
#     return render(request, '', context)

# def product_delete_view(request, my_id):
#     '''
#         # view to confirm delete i.e. if this given form is submitted then we delete object
#         <form action='.' method='POST'>
#             <h1>Do you want to delete the product "{{ object.title }}"?</h1>
#             <p>
#                 <input type='submit' value='Yes' />
#                 <a href='../'>Cancel</a>
#             </p>
#         </form>
#     '''
#     obj = get_object_or_404(Product, id=my_id)
#     if request.method == 'POST':
#         # confirming delete
#         obj.delete()
#         return redirect('../')
#     context = {
#         'object': obj
#     }
#     return redirect(request, '', context)


def product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    context = {
        'form': form
    }
    return render(request, 'products/create.html', context)


def product_detail_view(request):
    product = Product.objects.get(id=1)
    context = {
        'object': product
    }
    return render(request, 'products/detail.html', context)
