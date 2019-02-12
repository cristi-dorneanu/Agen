import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {CalculationComponent} from './calculation/calculation.component';
import {BenchmarksComponent} from './benchmarks/benchmarks.component';
import {AboutComponent} from './about/about.component';

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'calculation', component: CalculationComponent},
  {path: 'benchmarks', component: BenchmarksComponent},
  {path: 'about', component: AboutComponent},
  {path: '', pathMatch: 'full', redirectTo: '/home' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}

export const routingComponents = [HomeComponent, CalculationComponent, BenchmarksComponent, AboutComponent];
