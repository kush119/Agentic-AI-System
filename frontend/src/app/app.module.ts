import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { BrowserModule } from 'node_modules/@angular/platform-browser/types/_browser-chunk';
import { NgModule } from 'node_modules/@angular/core/types/_discovery-chunk';

@NgModule({
  declarations: [],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}