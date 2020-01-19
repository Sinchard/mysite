from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView

from .models import Fiction, Chapter, Content


class PostListView(ListView):
    queryset = Fiction.objects.all().order_by('fiction_id')
    context_object_name = 'page_obj'
    paginate_by = 50
    template_name = 'reader/index.html'


def index(request):
    print('fiction view')
    fictions = Fiction.objects.all()
    paginator = Paginator(fictions, 50)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'reader/index.html', {'page_obj': posts, 'page': page, 'title': '小说列表'})


def getChapter(request, fid):
    print('chapter view')
    fiction = Fiction.objects.filter(fiction_id=fid)[0]
    chapters = Chapter.objects.filter(fiction_id=fid).order_by("chapter_id")
    return render(request, 'reader/chapter.html', {'fiction': fiction, 'chapters': chapters})


def getContent(request, fid, cid):
    print('content view')
    chapter = Chapter.objects.filter(fiction_id=fid, chapter_id=cid)[0]
    content = Content.objects.filter(fiction_id=fid, chapter_id=cid)[0]
    return render(request, 'reader/content.html', {'chapter': chapter, 'content': content})
