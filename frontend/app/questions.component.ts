import { Component, OnInit, Input } from '@angular/core';
import { Question } from './question';
import { QuestionService } from './question.service';

@Component({
     selector:'polls-list',
     template:`
     <div>
        <label>Question:</label> <input #question_text />
        <button (click)="add(question_text.value); question_text.value=''">
          Add
        </button>
     </div>
     <ul class="polls">
     <li *ngFor=" let question of questions"(click)="onSelect(question)">
     <span class="badge">{{question.id}}</span> {{question.question_text}}
     </li>
     </ul>
     <question-detail [question]="selectedQuestion"></question-detail>
     <button (click)="save()">Save</button>
     `
})

export class QuestionsComponent implements OnInit{
polls_title='Poll Questions';
questions: Question[];
  selectedQuestion: Question;
  constructor(private questionService: QuestionService) { }
  getQuestions(): void {
    this.questionService.getQuestions().subscribe(questions => this.questions = questions);

  }
  ngOnInit(): void {
    this.getQuestions();
  }
    onSelect(question: Question): void {
    this.selectedQuestion = question;
  }
  save():void{
    this.questionService.update(this.selectedQuestion);
  }
  add(question_text: string): void {
  question_text = question_text.trim();
  if (!question_text) { return; }
  this.questionService.create(question_text);
}

}
