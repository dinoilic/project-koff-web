from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .users.views import UserViewSet, UserCreateViewSet
from .koff.views import CategoryList, CategoryDetail, BusinessEntities, validate_token, get_user_pk, get_user_comment_and_rating, \
BusinessEntityDetail, BusinessEntitySearchView, RatingsAndComments, RatingsAndCommentsList, RatingsAndCommentsDetail, TokenDetail

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'token', TokenDetail)
router.register(r'categories', CategoryList)
router.register(r'categories', CategoryDetail)
router.register(r'entities/search', BusinessEntitySearchView, 'EntitySearch')
router.register(r'entities', BusinessEntities, 'Entities')
router.register(r'entities', BusinessEntityDetail, 'Entities')
router.register(r'ratings-and-comments', RatingsAndComments, 'Ratings and Comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/token-validation/', validate_token),
    path('api/v1/get-user-pk/', get_user_pk),
    path('api/v1/get-user-comment-and-rating/', get_user_comment_and_rating),
    path('api/v1/ratings-and-comments-list/', RatingsAndCommentsList.as_view()),
    path('api/v1/ratings-and-comments/<int:pk>/', RatingsAndCommentsDetail.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
