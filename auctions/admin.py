from django.contrib import admin

from auctions.models import Comment, Listing, Bids, User, Watchlist

# Register your models here.
admin.site.register(Listing)
admin.site.register(Bids)
admin.site.register(User)
admin.site.register(Watchlist)
admin.site.register(Comment)