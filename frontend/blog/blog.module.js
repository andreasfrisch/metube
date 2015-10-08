'use strict';

angular.module('blog', [
	'blogView',
	'blogArchive',
	'blogCreate'
])
.constant('paragraphTypes', [
	'header',
	'text',
	'image'
]);