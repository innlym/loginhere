from django.conf.urls import patterns, url
import django.contrib.auth.views as authviews
import views


urlpatterns = patterns('',
    url(r'^$', views.profile, name='accounts'),
    url(r'^login/$', authviews.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', authviews.logout, {'next_page': '/'}, name='logout'),

    url(r'^password_change/$', authviews.password_change,
        {'template_name': 'accounts/password_change.html'}, name='password_change'),

    url(r'^password_change_done/$', authviews.password_change_done,
        {'template_name': 'accounts/password_change_done.html'}, name='password_change_done'),

    url(r'^password_reset/$', authviews.password_reset, 
        {'template_name': 'accounts/password_reset.html',
         'from_email': 'test@innlym.me'}, name='password_reset'),

    url(r'^password_reset_done/$', authviews.password_reset_done, 
        {'template_name':'accounts/password_reset_done.html'}, name='password_reset_done'),

    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', authviews.password_reset_confirm,
        {'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),

    url(r'^password_reset_complete/$', authviews.password_reset_complete, 
        {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),

    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^avatar/$', views.avatar, name='avatar'),
)