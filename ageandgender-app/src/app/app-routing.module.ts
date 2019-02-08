import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {CalculationComponent} from './calculation/calculation.component';
import {BenchmarksComponent} from './benchmarks/benchmarks.component';
import {CalculationInputComponent} from './calculation/calculation-input/calculation-input.component';
import {CalculationResultComponent} from './calculation/calculation-result/calculation-result.component';

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'calculation', component: CalculationComponent},
  {path: 'benchmarks', component: BenchmarksComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}

export const routingComponents = [HomeComponent, CalculationComponent, BenchmarksComponent, CalculationInputComponent,
  CalculationResultComponent];
