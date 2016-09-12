import { Injectable } from '@angular/core';
import { Headers, Response,RequestOptions, Http,HTTP_PROVIDERS } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/Rx';
// Observable class extensions
import 'rxjs/add/observable/of';
import 'rxjs/add/observable/throw';
// Observable operators
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/distinctUntilChanged';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/filter';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/switchMap';

import 'rxjs/add/operator/toPromise';

import { Question } from './question';
import {contentHeaders} from '../headers'


@Injectable()
export class QuestionService {

private apiUrl = 'http://127.0.0.1:8000/api/polls';  // URL to web api
private createQuestionUrl='http://127.0.0.1:8000/api/polls/create_question/';
private questionUrl='question/';

private updateHeaders = new Headers({'Content-Type': 'application/json'});

constructor(private http: Http) { }
getQuestions(): Observable<Question[]> {
    return this.http.get(this.apiUrl,{headers:contentHeaders})
                .map((res:Response) => res.json());
               //.catch((error:any) => Observable.throw(error.json().error || 'Server error'
  }

update(question: Question): Observable<Question[]> {
  const url = `${this.apiUrl}/${question.id}/${this.questionUrl}`;
  let saveHeaders = new Headers({'Content-Type': 'application/json'});
  saveHeaders.append('Accept','application/json');
  return this.http.patch(url, JSON.stringify(question), {headers: saveHeaders})
    .map((res:Response) => res.json());

}

 create(question_text: string): Observable<Question[]> {
 this.updateHeaders.append('Accept','application/json');
    return this.http
      .post(this.createQuestionUrl, JSON.stringify({question_text: question_text}), {headers: this.updateHeaders})
      .map((res:Response) => res.json())
      .catch(this.handleError);
}

delete(id: number) {
//this.updateHeaders.append('Accept','application/json');
  const url = `${this.apiUrl}/${id}/${this.questionUrl}`;
  return this.http.delete(url);
    //.map((res:Response) => res.json());

}


  private handleError (error: any) {
    // In a real world app, we might use a remote logging infrastructure
    // We'd also dig deeper into the error to get a better message
    let errMsg = (error.message) ? error.message :
      error.status ? `${error.status} - ${error.statusText}` : 'Server error';
    console.error(errMsg); // log to console instead
    return Observable.throw(errMsg);
  }

}
