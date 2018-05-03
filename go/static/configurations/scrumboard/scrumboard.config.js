(function() {
  'use strict';
  angular.module('scrumboard.demo').run(['$http', start_csrf]);

  function start_csrf ($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
