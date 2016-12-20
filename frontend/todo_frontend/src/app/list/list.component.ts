import { Component, OnInit } from '@angular/core';
import {ToDosService} from '../todos.service';

@Component({
  selector: 'todo-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css'],
  providers: [ToDosService],
})
export class ListComponent implements OnInit {

  constructor(private todosservice: ToDosService) { }
  getToDos(){
    this.todosservice.getToDos()
    .then(todos => this.todos = todos)
    .catch(error => this.error = error);
  }

  todos: any[];
  selectedToDo: any;
  error: string;

  ngOnInit() {
    this.getToDos();
  }

  clickedToDo(todo){
    this.selectedToDo = todo;
  }

}
