import React from 'react'

const Header = () => {
  return (
    <header className='flex justify-evenly items-center flex-col w-full lg:h-52 h-32 bg-antiquewhite'>
      <img src="src\img\logo.png" alt="logo"></img>
      <h1 className='lg:text-4xl text-2xl font-semibold'>
          Hệ thống dự đoán tính cách
      </h1>
    </header>
  )
}

export default Header