import { Component } from '@angular/core';
import { HTTP_PROVIDERS } from '@angular/http';


@Component({
    selector: 'my-app',
    template: `<h1>Voting Tutorial</h1>
    <polls-list></polls-list>

    `,
     providers:[HTTP_PROVIDERS]
})
export class AppComponent{
  title = 'Voting Tutorial';

}
