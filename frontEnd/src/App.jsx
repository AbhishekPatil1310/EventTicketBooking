import { useState } from 'react'
import './App.css'
import EventList from './components/Event'
import Event from './pages/events'
import Home from './pages/home'
import {Route,BrowserRouter as Router,Routes } from 'react-router-dom'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Router>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/Event' element={<EventList />} />
        <Route path='/events' element={<Event/>} />
      </Routes>
    </Router>
    </>
  )
}

export default App
