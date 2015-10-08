//frontend/blog/blogMenu.controller.js
'use strict';

angular.module('blog')
.controller('blogMenu', ['menuService', function(menuService) {
	menuService.removeLinks();
	menuService.addLinks([
		{
			title: 'Archive',
			state: 'blog.archive',
		},
		{
			title: 'New post',
			state: 'blog.create.content',
			stateRoot: 'blog.create'
		}
	]);
}]);