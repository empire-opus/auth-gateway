// types.ts
export interface User {
  id: string;
  username: string;
  email: string;
  password: string;
  role: 'admin' | 'user';
}

export interface AuthToken {
  token: string;
  expiresAt: number;
}

export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  user: User;
  token: AuthToken;
}

export interface RegistrationRequest {
  username: string;
  email: string;
  password: string;
}

export interface RegistrationResponse {
  user: User;
  token: AuthToken;
}

export enum AuthErrorType {
  InvalidCredentials,
  UserAlreadyExists,
  InvalidToken,
}

export interface AuthError {
  type: AuthErrorType;
  message: string;
}