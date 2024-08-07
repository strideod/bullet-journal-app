import { format } from 'date-fns';

async function getDailyLog() {
  const response = await fetch('http://127.0.0.1:8000/entries/daily', {cache: 'no-store'});
  // The return vale is 'not' serialized
  // You can return Date, Map, Set, etc.

  if (!response.ok) {
    // This will actiave the closest 'error.js" Error Boundary
    throw new Error('Failed to fetch data')
  }

  return response.json()
}

const getIcon = (type: string) => {
  switch (type) {
    case 'task':
      return '•'; // Bullet for task
    case 'note':
      return '–'; // Medium dash for note
    case 'event':
      return '○'; // Circle for event
    default:
      return '';
  }
}

export default async function Home() {
  const dailyLog = await getDailyLog();

  const today = new Date();
  const formattedDate = format(today, 'M.d.EE');

  return (
    <div>
      <h1>Daily Log</h1>
      <p>{formattedDate}</p>
      <ul>
        {dailyLog.map((entry: any) => (
          <li key={entry.id}>
          <h2>{getIcon(entry.type)} {entry.description} {entry.event_time}</h2>
          {/* Render additional fields as needed */}
        </li>
        ))}
      </ul>
    </div>
  );
}
