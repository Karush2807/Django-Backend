import React, { Component } from "react";
import { createRoot } from "react-dom/client";

export default class App extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return(<h1>Testing React Code</h1>);
    }
}

const container = document.getElementById("app");
const root = createRoot(container); // Create a root
root.render(<App />); // Render your App component