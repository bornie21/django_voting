import { Component, OnInit, Input } from '@angular/core';
import { Question } from './question';
import { QuestionService } from './question.service';

@Component({
     selector:'polls-list',
     //template:` `
     templateUrl: 'app/questions/questions.component.html',
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
    const update$ =this.questionService.update(this.selectedQuestion);
    update$.subscribe(
    data => {
           // refresh the list
           //this.getQuestions();
           this.selectedQuestion = null;
           return true;
         }
    );
  }
 add(question_text: string): void {
  question_text = question_text.trim();
  if (!question_text) { return; }
  const add$=this.questionService.create(question_text);
  add$.subscribe(
  data => {
           // refresh the list
           this.getQuestions();
           return true;
         }
   //newQuestion  => this.questions.push(newQuestion)
   );
}
delete(question: Question): void {
    const delete$=this.questionService.delete(question.id);
    if (confirm("Are you sure you want to delete this question: " + question.question_text + "?")) {
    delete$.subscribe(
    data => {
           // refresh the list
           this.questions = this.questions.filter(q => q !== question);
           if (this.selectedQuestion === question) { this.selectedQuestion = null; }
           //this.getQuestions();
           return true;
         }
    );
  }
  }

}
