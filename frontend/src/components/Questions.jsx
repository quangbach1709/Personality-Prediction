import React, { useState } from 'react'
import { questions, answers } from '../constants'

const Questions = () => {
  const [answer, setAnswer] = useState([]);
  const [gender, setGender] = useState(null);
  const [age, setAge] = useState(null);

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
      alert(data["result"])
    })
    .catch((error) => {
      console.error('Lỗi:', error);
    });
    
  }

  return (

    <div class="question">
      <div style={{display: 'flex', alignItems: 'center'}}>
        <p>Giới tính:</p>
        <input onChange={(e) => {setGender(parseInt(e.target.value))}} type="radio" name="gender" id="male" value={1}/>
        <label htmlFor="male">Nam</label>
        <input onChange={(e) => {setGender(parseInt(e.target.value))}} type="radio" name='gender' id='female' value={0} />
        <label htmlFor="female">Nữ</label>
      </div>
      <div style={{display: 'flex', alignItems: 'center'}}>
        <label htmlFor="age">Tuổi</label>
        <input onChange={(e) => {setAge(parseInt(e.target.value))}} type="number" name="age" id='age' value={age}/>
      </div>
      <ol>
        {questions.map((question, questionIndex) => (
          <li key={questionIndex}>
            <p className='font-semibold'>{question.label}</p>
              {answers.map((answer, answerIndex) => (
                <div key={answerIndex}>
                  <input onChange={() => handleAnswerChange(questionIndex, answer.value)} value={answer.value} type="radio" name={`question_${questionIndex}`} id={`answerQuestion_${answerIndex}`} />
                  <label htmlFor={`answerQuestion_${answerIndex}`}>{answer.label}</label>
                </div>
              ))}
          </li>
        ))}
      </ol>
      <div>
        <button onClick={handleSubmit}>Xác nhận</button>
      </div>

    </div>
  )
}

export default Questions