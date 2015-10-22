//frontend/blog/blogMenu.controller.js
'use strict';

angular.module('blog')
.controller('blogMenu', ['menuService', 'authenticationStatus', function(menuService, authenticationStatus) {
	menuService.removeLinks();
	menuService.addLinks([
        {
            title: 'Newest',
            state: 'blog.newest',
            visible: true,
        },
		{
			title: 'Archive',
			state: 'blog.archive',
            visible: true,
		},
		{
			title: 'New post',
			state: 'blog.create.content',
			stateRoot: 'blog.create',
            visible: authenticationStatus.isAuthenticated,
		}
	]);
}]);