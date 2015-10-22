'use strict';

angular.module('blog', [
	'blogView',
	'blogArchive',
	'blogCreate',
    'blogNewest',
])
.constant('paragraphTypes', [
	'header',
	'text',
	'image'
]);