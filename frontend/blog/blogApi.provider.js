// frontend/blog/blogApi.service.js
'use strict';

angular.module('blog')
.provider('blogApi', function blogApiProvider() {
	var blogBackendEndpoint = 'undefined';
    
    this.setBackendEndpoint = function(url) {
        blogBackendEndpoint = url;
    }
    
    this.$get = ['$http', '$q', function($http, $q) {
        // API definition
    	return {
    		getAllPosts: _getAllPosts,
    		getFilteredPosts: _getFilteredPosts,
    		getSpecificPost: _getSpecificPost,
    		getSpecificPostById: _getSpecificPostById,
    		createNewPost: _createNewPost,
            getNewestPost: _getNewestPost,
    	};
	
    	// Function definitions:
    	// hoisted during runtime
	
        function _interpretPostContent(post) {
            post.date = Date(post.date_unix_seconds);
            return post;
        }
    
    	function _getAllPosts() {
    		var deferred = $q.defer();
    		//deferred.resolve(MOCKpostList);
    		$http.get(blogBackendEndpoint)
    		.then(
    			function(response) {
                    var posts = response.data
                    for (var index in posts) {
                        _interpretPostContent(posts[index]);
                    }
    				deferred.resolve(posts);
    			}
    			//handle error
    		);
    		return deferred.promise;
		
    	}
    	function _getFilteredPosts() {
    		var deferred = $q.defer();
    		deferred.reject(501);
    		return deferred.promise;
    	}
    
    	function _getSpecificPost(slug) {
    		var deferred = $q.defer();
    		//deferred.resolve(MOCKpostList[postId]);
    		$http.get(blogBackendEndpoint+slug)
    		.then(
    			function(response) {
    				deferred.resolve(_interpretPostContent(response.data));
    			}
    			//handle error
    		);
    		return deferred.promise;
    	}
    	function _getSpecificPostById(id) {
    		var deferred = $q.defer();
    		//deferred.resolve(MOCKpostList[postId]);
    		$http.get(blogBackendEndpoint+'id/'+id)
    		.then(
    			function(response) {
    				deferred.resolve(_interpretPostContent(response.data));
    			}
    			//handle error
    		);
    		return deferred.promise;
    	}
    
    	function _createNewPost(newPostData) {
            var deferred = $q.defer();
            newPostData.date_unix_seconds = new Date(newPostData.date).getTime() / 1000; //Convert time string to unix_seconds; TODO: Fix format: YYYY-MM-DD
    		$http.post(blogBackendEndpoint, newPostData)
            .then(
                function(response) {
                    console.log(response);
                    deferred.resolve(response.status);
                }
                //handle error
            )
        
            return deferred.promise;
    	}
	
        function _getNewestPost() {
            var deferred = $q.defer();
            $http.get(blogBackendEndpoint+'newest/')
            .then(
                function(response) {
                    deferred.resolve(response)
                }
                //handle error
            );
            return deferred.promise;
        }
    
    }]
});