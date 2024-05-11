import React from 'react'
import Header from './components/Header'
import Questions from './components/Questions'

const App = () => {
  return (
    <div className='lg:w-60vw flex items-center justify-center flex-col shadow-lg'>
    <Header />
    <Questions />
    </div>
  )
}

export default App