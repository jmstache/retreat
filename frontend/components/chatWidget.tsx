// components/ChatWidget.tsx
"use client";

import { useState } from "react";

export default function ChatWidget() {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState<{ role: string; text: string }[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = input;
    const newMessages = [...messages, { role: "user", text: userMessage }];
    setMessages(newMessages);
    setInput("");
    setLoading(true);

    const formattedHistory = newMessages.map((msg) => ({
      role: msg.role === "user" ? "user" : "assistant",
      content: msg.text
    }));

    const baseUrl = process.env.NEXT_PUBLIC_CHAT_API_URL || 'http://localhost:8000';
    const apiUrl = `${baseUrl}/chat`;
    console.log("➡️ Using Chat API:", apiUrl);

    try {
      const res = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ history: formattedHistory })
      });

      const data = await res.json();
      setMessages((prev) => [...prev, { role: "bot", text: data.response }]);
    } catch (e) {
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "Sorry, something went wrong." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div
        className="fixed bottom-6 right-6 z-50"
        onClick={() => setOpen(!open)}
      >
        <button className="bg-indigo-600 text-white px-4 py-2 rounded-full shadow-lg hover:bg-indigo-500">
          {open ? "×" : "Chat"}
        </button>
      </div>

      {open && (
        <div className="fixed bottom-20 right-6 w-80 bg-white shadow-xl rounded-lg p-4 flex flex-col h-[400px] z-50">
          <div className="overflow-y-auto flex-1 mb-2 space-y-2">
            {messages.map((msg, i) => (
              <div
                key={i}
                className={`text-sm p-2 rounded-md max-w-xs ${
                  msg.role === "user" ? "bg-indigo-100 self-end" : "bg-gray-100 self-start"
                }`}
              >
                {msg.text}
              </div>
            ))}
            {loading && <div className="text-sm italic">Thinking...</div>}
          </div>
          <div className="flex items-center gap-2">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              className="flex-1 border rounded px-2 py-1 text-sm"
              placeholder="Ask something..."
            />
            <button
              onClick={sendMessage}
              className="bg-indigo-600 text-white px-3 py-1 rounded text-sm hover:bg-indigo-500"
              disabled={loading}
            >
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
