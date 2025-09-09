import Head from 'next/head';
import TravelAssistant from '../components/TravelAssistant';

export default function Home() {
  return (
    <>
      <Head>
        <title>Travel Documentation Assistant</title>
        <meta name="description" content="AI-powered travel documentation helper" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <TravelAssistant />
    </>
  );
}