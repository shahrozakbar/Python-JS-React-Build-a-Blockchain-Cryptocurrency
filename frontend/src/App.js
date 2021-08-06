import React, {useState} from "react";
import Joke from "./Joke";

function App() {
    const [userQuery, setUserQuery] = useState('');

    const updateUserQuery = event => {
        setUserQuery(event.target.value);
        console.log('userQuery', userQuery);
    }

    const searchQuery = () => {
        window.open(`https://google.com/search?q=${userQuery}`);
    }

    const handleKeyPress = event => {
        if (event.key === 'Enter') {
            searchQuery()
        }
    }

    return (
        <div className="App">
           <input value={userQuery} onChange={updateUserQuery} onKeyPress={handleKeyPress}/>
            <button onClick={searchQuery} >Search</button>
            <div>{userQuery}</div>
            <hr/>
            <Joke />
        </div>
    );
}

export default App;
