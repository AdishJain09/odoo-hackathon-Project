import { useEffect, useState } from "react";
import axios from "axios";
import Link from "next/link";

export default function Home() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/questions").then(res => setQuestions(res.data));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">StackIt - Questions</h1>
      {questions.map(q => (
        <Link href={`/questions/${q._id}`} key={q._id}>
          <div className="border p-4 mb-2 cursor-pointer">
            <h2 className="font-semibold">{q.title}</h2>
            <p className="text-sm text-gray-500">Tags: {q.tags.join(', ')}</p>
          </div>
        </Link>
      ))}
    </div>
  );
}
