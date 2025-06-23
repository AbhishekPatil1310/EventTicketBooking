import { useState } from 'react'
import './App.css'
import Event from './pages/events'
import Home from './pages/home'
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/events' element={<Event />} />
      </Routes>
    </Router>
  )
}

export default App
