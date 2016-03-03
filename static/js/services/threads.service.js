Intern.factory('ThreadsService', ThreadsService);


function ThreadsService($http) {

  function create(post) {
    return $http.post('/api/threads/', post);
  }

  function list() {
    return $http.get('/api/threads/');
  }

  function get(id) {
    return $http.get('/api/threads/' + id + '/', post);
  }

  function update(id, post) {
    return $http.put('/api/threads/' + id + '/', post);
  }

  function destroy(id) {
    return $http.delete('/api/threads/' + id + '/');
  }

  return {
    create: create,
    list: list,
    update: update,
    destroy: destroy
  };
}
