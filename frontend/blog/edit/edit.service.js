// frontend/blog/create/edit.service.js
'use strict';

angular.module('blogEdit')
.service('blogEditService', ['$state', '$q', 'blogApi', function($state, $q, blogApi) {
    var that = this;
	this.blogPostDraft = {};
	this.editting_existing = false;
    this.editting_existing_id = null;
    
	this.getDraft = function() {
        return this.blogPostDraft;
	};
	
	this.setDraft = function(draft) {
		this.blogPostDraft = draft;
	};
    
    this.cleanDraft = function() {
        this.blogPostDraft = {};
        this.editting_existing = false;
    }
    
    this.submitPost = function() {
		blogApi.createNewPost(this.blogPostDraft)
		.then(
			function() {
                this.cleanDraft();
				$state.go('blog.archive');
			}
		);
    }
    
    this.getExistingPost = function(id) {
        var deferred = $q.defer();
        if (isNaN(parseInt(id))) {
            deferred.resolve('ok');
        } else {
            if (that.editting_existing_id == parseInt(id)) {
                deferred.resolve('ok');
            } else {
                blogApi.getSpecificPostById(id).then(
            		 //success
            		function(postObject) {
                        that.editting_existing = true;
            			that.blogPostDraft = postObject;
                        deferred.resolve('ok');
            		}
            		//handle error
            	);
            }
        }
		return deferred.promise;
    };
}]);