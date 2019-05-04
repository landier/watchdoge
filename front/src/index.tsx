import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';
import 'bootstrap/js/dist/alert';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(
    <div>
        <div className="alert alert-warning alert-dismissible fade show" role="alert">
            <button type="button" className="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
            <strong>Holy guacamole!</strong> You should check in on some of those fields below.
        </div>
        <p>Hello World</p>
    </div>, document.getElementById('boum'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
