import { Component, Input } from '@angular/core';
import { Question } from './question';

@Component({
  selector:'question-detail',
  template:`
            <div *ngIf="question">
              <h2>Question details!</h2>
              <div><label>id: </label>{{question.id}}</div>
              <div>
                <label>name: </label>
                <input [(ngModel)]="question.question_text" placeholder="question text"/>
              </div>
           </div>

  `
})
export class QuestionDetailComponent {
@Input()
question: Question;

}
