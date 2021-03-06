# -*- coding: utf-8 -*-
# This file is part of Shuup CMS Blog Addon.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf.urls import url

from shuup_cms_blog.views import (
    AddSavedArticlesView, RemoveSavedArticlesView, SavedArticlesView
)

urlpatterns = [
    url(r"^dashboard/saved-articles/$", SavedArticlesView.as_view(), name="shuup-cms-blog.saved-articles"),
    url(
        r"^dashboard/saved-article/(?P<pk>.+?)/add/$",
        AddSavedArticlesView.as_view(),
        name="shuup-cms-blog.add-saved-article"
    ),
    url(
        r"^dashboard/saved-article/(?P<pk>.+?)/remove/$",
        RemoveSavedArticlesView.as_view(),
        name="shuup-cms-blog.remove-saved-article"
    )
]
