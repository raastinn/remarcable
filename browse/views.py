from django.shortcuts import render
from .models import Product, Category, Tag

def product_list(request):
    # fetches all products including their related category (foreign key) and tags (many to many)
    products = Product.objects.select_related("category").prefetch_related("tags").all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    search_query = request.GET.get("search", "").strip()
    category_id = request.GET.get("category", "").strip()
    tag_ids = request.GET.getlist("tags")

    if search_query:
        products = products.filter(description__contains=search_query)

    if category_id:
        products = products.filter(category_id=category_id)

    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()

    context = {
        "products": products,
        "categories": categories,
        "tags": tags,
        "search_query": search_query,
        "selected_category": category_id,
        "selected_tags": [int(tag_id) for tag_id in tag_ids if tag_id.isdigit()],
    }

    return render(request, "base.html", context)
