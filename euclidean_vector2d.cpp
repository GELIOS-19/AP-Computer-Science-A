#ifndef CHESS_ENGINE_HPP
#define CHESS_ENGINE_HPP

/////////////////////////////////////////////////////////////
/// Headers
/////////////////////////////////////////////////////////////
#include "../Shared/Libraries.hpp"

namespace chess {

////////////////////////////////////////////////////////////
/// \brief Contains all OpenGL functionality
///
////////////////////////////////////////////////////////////
namespace engine {

namespace priv {

////////////////////////////////////////////////////////////
/// \brief Callback function for the engine window
///
/// \param window Window the callback function is called for
/// \param frameBufferWidth Width of the frame buffer
/// \param frameBufferHeight Height of the frame buffer
/// 
////////////////////////////////////////////////////////////
static void frameBufferSizeCallback(GLFWwindow* window, int frameBufferWidth, int frameBufferHeight) {
  glViewport(0, 0, frameBufferWidth, frameBufferHeight);
}

} // namespace priv

////////////////////////////////////////////////////////////
/// \brief Creates a window with GLFW and GLEW and sets it to engineWindow
///
/// Requires glfwInit() to be called prior to calling this method.
///
/// \throws GLEW initialization error
///
/// \param windowWidth Width of the window
/// \param windowHeight Height of the window
/// \param windowTitle Title of the window
/// \param frameBufferWidth Width of the frame buffer
/// \param frameBufferHeight Height of the frame buffer
/// \param makeResizable Indicates if the window should be made resizable
/// 
////////////////////////////////////////////////////////////
static GLFWwindow* createWindow(const int windowWidth,
                                const int windowHeight,
                                const std::string windowTitle,
                                int frameBufferWidth,
                                int frameBufferHeight,
                                const bool makeResizable) {
  // Create Window
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
  glfwWindowHint(GLFW_RESIZABLE, makeResizable ? GL_TRUE : GL_FALSE);

  GLFWwindow* window = glfwCreateWindow(windowWidth,
                                        windowHeight,
                                        windowTitle.c_str(),
                                        nullptr,
                                        nullptr);

  if (makeResizable) {
    glfwSetFramebufferSizeCallback(window, priv::frameBufferSizeCallback);
  } else {
    glfwGetFramebufferSize(window, &frameBufferWidth, &frameBufferHeight);
    glViewport(0, 0, frameBufferWidth, frameBufferHeight);
  }
  
  glfwMakeContextCurrent(window);

  // Initialize GLEW
  glewExperimental = GL_TRUE;
  if (glewInit() != GLEW_OK) {
    glfwTerminate();
    throw "Error :: Engine.cpp :: GLEW initialization failed";
  }

  return window;
}

////////////////////////////////////////////////////////////
/// \brief Calls methods preliminary to drawing
///
/// \param window Window to affect
///
////////////////////////////////////////////////////////////
static void beginWindowDraw(GLFWwindow* window) {
  // Make the window current context if it is not already
  if (window != glfwGetCurrentContext())
    glfwMakeContextCurrent(window);
  
  glClearColor(0.f, 0.f, 0.f, 1.f); // The color used here does not matter
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT);
}

////////////////////////////////////////////////////////////
/// \brief Calls methods after drawing
///
/// \param window Window to affect
///
////////////////////////////////////////////////////////////
static void endWindowDraw(GLFWwindow* window) {
  // Make the window current context if it is not already
  if (window != glfwGetCurrentContext())
    glfwMakeContextCurrent(window);
  
  glfwSwapBuffers(window);
  glFlush();
}

} // namespace engine
} // namespace chess


#endif // #ifndef CHESS_ENGINE_HPP
