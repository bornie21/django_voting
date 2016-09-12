import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule }    from '@angular/http';
import { FormsModule }   from '@angular/forms';
import { AppComponent }  from './app.component';

import { QuestionsComponent} from './questions/questions.component';
import { QuestionDetailComponent} from './questions/question-detail.component';
import { QuestionService} from './questions/question.service';

@NgModule({
  imports: [ BrowserModule,
  HttpModule,
  FormsModule
  ],
  declarations: [
  AppComponent,
  QuestionsComponent,
  QuestionDetailComponent
  ],
  providers: [QuestionService ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
