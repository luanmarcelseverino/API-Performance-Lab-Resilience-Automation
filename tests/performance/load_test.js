import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 20 }, // Sobe para 20 usuários
    { duration: '1m', target: 20 },  // Mantém 20 usuários
    { duration: '30s', target: 0 },  // Desce para 0
  ],
};

export default function () {
  let payload = JSON.stringify({
    email: 'fulano@qa.com',
    password: 'teste',
  });

  let params = {
    headers: { 'Content-Type': 'application/json' },
  };

  let res = http.post('https://serverest.dev/login', payload, params);
  
  check(res, {
    'status is 200': (r) => r.status === 200,
    'transaction time < 500ms': (r) => r.timings.duration < 500,
  });
  
  sleep(1);
}