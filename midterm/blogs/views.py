from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Blog
import json

@csrf_exempt
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        blog_list = []
        for blog in blogs:
            blog_list.append({
                'id': blog.id,
                'title': blog.title,
                'description': blog.description,
                'owner': blog.owner
            })
        return JsonResponse(blog_list, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        owner = data.get('owner')
        if title and description and owner:
            blog = Blog.objects.create(
                title=title,
                description=description,
                owner=owner
            )
            return JsonResponse({
                'id': blog.id,
                'title': blog.title,
                'description': blog.description,
                'owner': blog.owner
            }, status=201)
        else:
            return JsonResponse({'error': 'Invalid data provided.'}, status=400)

@csrf_exempt
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'GET':
        return JsonResponse({
            'id': blog.id,
            'title': blog.title,
            'description': blog.description,
            'owner': blog.owner
        })

    elif request.method == 'PUT':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        owner = data.get('owner')
        if title and description and owner:
            blog.title = title
            blog.description = description
            blog.owner = owner
            blog.save()
            return JsonResponse({
                'id': blog.id,
        .        'title': blog.title,
                'description': blog.description,
                'owner': blog.owner
            })
        else:
            return JsonResponse({'error': 'Invalid data provided.'}, status=400)

    elif request.method == 'DELETE':
        blog.delete()
        return JsonResponse({'message': 'Blog deleted successfully.'}, status=204)
