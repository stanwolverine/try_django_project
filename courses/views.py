from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm
# Create your views here.

# class based view

# To reduce the redundant code use and read about mixins


class CourseDeleteView(View):
    template_name = 'courses/course_delete.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    # FOR GET REQUEST ON THIS VIEW
    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    # FOR POST REQUEST ON THIS VIEW
    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)


class CourseUpdateView(View):
    template_name = 'courses/course_update.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    # FOR GET REQUEST ON THIS VIEW
    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    # FOR POST REQUEST ON THIS VIEW
    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    # FOR GET REQUEST ON THIS VIEW
    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    # FOR POST REQUEST ON THIS VIEW
    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.object.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


# class MyListView(CourseListView):
#     queryset = Course.object.filter(id=1)


class CourseView(View):
    template_name = 'about.html'

    # FOR GET REQUEST ON THIS VIEW
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            '''
            i.e. if id is passed than we want detail view to render
            if id is not passed than we want our default template to render
            '''
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

    # FOR POST REQUEST ON THIS VIEW
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


# Functional view


def course_view(request):
    return render(request, 'about.html', {})
