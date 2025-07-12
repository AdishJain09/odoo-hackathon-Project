import { useState } from "react";
import Editor from "../components/Editor";
import axios from "axios";

export default function Ask() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [tags, setTags] = useState("");

  const submitQuestion = async () => {
    const token = localStorage.getItem("token");
    await axios.post("http://localhost:5000/questions", {
      title,
      description,
      tags: tags.split(",").map(t => t.trim())
    }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert("Posted!");
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-2">Ask a Question</h1>
      <input placeholder="Title" className="border p-2 w-full mb-2" value={title} onChange={e => setTitle(e.target.value)} />
      <Editor content={description} onChange={setDescription} />
      <input placeholder="Tags (comma-separated)" className="border p-2 w-full mt-2" value={tags} onChange={e => setTags(e.target.value)} />
      <button onClick={submitQuestion} className="bg-blue-600 text-white mt-4 p-2 rounded">Submit</button>
    </div>
  );
}
