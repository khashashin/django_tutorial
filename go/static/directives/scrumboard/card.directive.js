(function() {
  'use strict';

  angular.module('scrumboard.demo').directive('scrumboardCard', CardDirective);

  function CardDirective() {
    return {
      templateUrl: '/static/directives/scrumboard/card.html',
      restrict: 'E',
      controller: ['$scope', '$http', function($scope, $http) {
        var url = '/scrumboard/cards/' + $scope.card.id + '/';
        $scope.update = function() {
          $http.put(
            url,
            $scope.card
          );
        };
      }]
    };
  }
})();