
export class Quiz{

    constructor(
        title,
        questions,
        id
    ){
        this.title = title;
        this.questions = questions;
        this.id = id;
    }

    addQuestion(question){
        this.questions.push(question);
    }

}