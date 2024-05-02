import React from 'react'

const Header = () => {
  return (
    <header className='flex justify-around items-center h-20 bg-gradient-to-r from-yellow-500 bg-yellow-900'>
      <img src="src\img\logo.png" alt="logo"></img>
      <h1 className='lg:text-3xl sm:text-2xl text-white uppercase'>
          Hệ thống dự đoán tính cách
      </h1>
        {/* <i className='lg:text-3xl sm:text-2xl text-white uppercase tracking-wide'>64ktpm4</i> */}
    </header>
  )
}

export default Header