import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class ToDosService {

  private apiURL = 'http://localhost:8000/todos/'
  constructor(private http: Http) { }
  getToDos() {
    /*return Promise.resolve([
    {
      "example": "1",
    },
    {
      "example": "2",
    },
  ]);*/
    return this.http.get(this.apiURL)
                .toPromise()
                .then(response => response.json().results)
                .catch(this.handleError);
  }

  private handleError(error: any) {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
}
