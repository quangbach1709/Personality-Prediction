import React, { useState } from 'react'
import { questions, answers } from '../constants'
import Notification from './Notification';

const Questions = () => {
  const [answer, setAnswer] = useState([]);
  const [gender, setGender] = useState(null);
  const [age, setAge] = useState(null);
  const [personality, setPersonality] = useState(null);

  const handleAnswerChange = (questionIndex, answerValue) => {
    setAnswer(oldAns => {
      const newAns = [...oldAns];
      newAns[questionIndex] = answerValue;
      return newAns;
    })
  };

  const handleSubmit = () => {
    const answerE = answer.slice(0, 10);
    const answerA = answer.slice(10, 20);
    const answerC = answer.slice(20, 30);
    const answerN = answer.slice(30, 40);
    const answerO = answer.slice(40, 50);

    const scoreE = Math.round(answerE.reduce((sum, answerEVal) => sum + answerEVal, 0) * 0.16);
    const scoreA = Math.round(answerA.reduce((sum, answerEVal) => sum + answerEVal, 0) * 0.16);
    const scoreC = Math.round(answerC.reduce((sum, answerEVal) => sum + answerEVal, 0) * 0.16);
    const scoreN = Math.round(answerN.reduce((sum, answerEVal) => sum + answerEVal, 0) * 0.16);
    const scoreO = Math.round(answerO.reduce((sum, answerEVal) => sum + answerEVal, 0) * 0.16);

    /*const features = {
      Gender: gender,
      Age: age,
      E: scoreE,
      A: scoreA,
      C: scoreC,
      N: scoreN,
      O: scoreO
    }*/
    const features = {
      Gender: 1,
      Age: 20,
      E: 4,
      A: 8,
      C: 5,
      N: 4,
      O: 1
    }

    console.log(features);
    fetch('http://127.0.0.1:5000/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(features),
    })
    .then(response => response.json())
    .then(data => {
      // alert(data["result"])
      setPersonality(data['result'])
    })
    .catch((error) => {
      console.error('Lỗi:', error);
    });
    
  }

  return (
    
    <div class="bg-white w-full p-9 flex justify-center flex-col gap-y-3 lg:text-lg text-sm">
      {personality && (
        <Notification personality={personality} />
      )}
      <div className='flex items-center gap-3'>
        <p>Giới tính:</p>
        <input onChange={(e) => {setGender(parseInt(e.target.value))}} type="radio" name="gender" id="male" value={1}/>
        <label htmlFor="male">Nam</label>
        <input onChange={(e) => {setGender(parseInt(e.target.value))}} type="radio" name='gender' id='female' value={0} />
        <label htmlFor="female">Nữ</label>
      </div>
      <div className='flex items-center gap-3'>
        <label htmlFor="age">Tuổi</label>
        <input className='border border-black rounded-md w-20' onChange={(e) => {setAge(parseInt(e.target.value))}} type="number" name="age" id='age' value={age}/>
      </div>
      <ol className='list-decimal font-semibold flex flex-col gap-y-3'>
        {questions.map((question, questionIndex) => (
          <li className='ml-3' key={questionIndex}>
            <p className='font-semibold'>{question.label}</p>
              {answers.map((answer, answerIndex) => (
                <div className='font-normal my-1' key={answerIndex}>
                  <input onChange={() => handleAnswerChange(questionIndex, answer.value)} value={answer.value} type="radio" name={`question_${questionIndex}`} id={`answerQuestion_${answerIndex}`} />
                  <label className='ml-1' htmlFor={`answerQuestion_${answerIndex}`}>{answer.label}</label>
                </div>
              ))}
          </li>
        ))}
      </ol>
      <div className='flex justify-center items-center mt-3'>
        <button className='p-2 rounded-md bg-sky-500 text-white' onClick={handleSubmit}>Xác nhận</button>
      </div>

    </div>
  )
}

export default Questions