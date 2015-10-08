'use strict';

angular.module('blogView')
.directive('blogParagraph', function () {
	return {
		restrict: 'E',
		scope: {
			paragraph: '=',
			first: '='
		},
		templateUrl: '/static/blog/view/paragraph.html',
	};
});