
# from django.contrib import admin
# from django.urls import path

# from tt.views import team_view
# from tt.views import left
# from tt.views import home


# urlpatterns = [
#     path('teams/', team_view, name='team-view'),
#     path('',views.home),
#     path('admin/', admin.site.urls),
#     path('left/', left, name='left'), 
    
#     #    path('', include('TaskTracker.urls')),
# ]


from django.contrib import admin
from django.urls import path

from tt.views import team_view, left, home,dataTeam # Import 'home' along with 'team_view' and 'left'

urlpatterns =[
    path('teams/', team_view, name='team-view'),
    path('', home, name='home'),
      path('dataTeam/',dataTeam,name='dataTeam'), # Specify 'home' as the view for the root URL
    path('admin/', admin.site.urls),
    path('left/', left, name='left'),
    # Other URL patterns go here
]






