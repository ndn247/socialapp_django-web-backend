from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin
from models import Post
from mezzanine.generic.models import ThreadedComment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
	#readonly_fields = ("publish_date")
	list_display = ("id", "title", "owner", "publish_date", "comments_count", "rating_sum")
	list_display_links = ("title",)
	ordering = ("-publish_date",)
	list_filter = ("owner__username",)
	list_editable = None

	fieldsets = (
        (None, {
			"fields": ('title', 'message', 'owner', 'publish_date', 'related_posts'),
		}),
    )


admin.site.register(Post, PostAdmin)