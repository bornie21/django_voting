import { Component, Input } from '@angular/core';
import { Question } from './question';

@Component({
  selector:'question-detail',
  templateUrl: 'app/questions/question-detail.component.html',
})
export class QuestionDetailComponent {
@Input()
question: Question;

}
