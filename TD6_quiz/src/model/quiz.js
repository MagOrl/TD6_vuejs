
import { Question } from "./question.js";

export class Quiz{

    constructor(
        title,
        questions,
        url
    ){
        this.title = title;
        this.questions = questions;
        this.url = url;
    }

    addQuestion(question){
        this.questions.push(question);
    }

}