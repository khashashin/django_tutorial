(function() {
  'use strict';
  angular.module('scrumboard.demo').config(['$routeProvider', config]).run(['$http', start_csrf]);

  function config($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: '/static/angular_templates/scrumboard/scrumboard.html',
        controller: 'ScrumboardController',
      })
      .when('/login', {
        templateUrl: '/static/angular_templates/scrumboard/login.html'
      })
      .otherwise('/');
  }

  function start_csrf ($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
